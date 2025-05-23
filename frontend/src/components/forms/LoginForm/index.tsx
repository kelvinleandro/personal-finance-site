"use client";

import { Field, Input, Stack } from "@chakra-ui/react";
import { loginAction } from "@/actions/login-action";
import LoginButton from "./LoginButton";

const LoginForm = () => {
  const handleFormAction = async (formData: FormData) => {
    try {
      await loginAction(formData);
    } catch (error) {
      alert(error);
    }
  };

  return (
    <form action={handleFormAction}>
      <Stack gap={4}>
        <Field.Root>
          <Field.Label color="black">Email</Field.Label>
          <Input
            type="email"
            name="email"
            required
            color="black"
            placeholder="Enter your email"
            _placeholder={{ color: "gray.500" }}
            px={2}
          />
        </Field.Root>

        <Field.Root>
          <Field.Label color="black">Password</Field.Label>
          <Input
            type="password"
            name="password"
            required
            color="black"
            placeholder="Enter your password"
            _placeholder={{ color: "gray.500" }}
            px={2}
          />
        </Field.Root>

        <LoginButton />
      </Stack>
    </form>
  );
};

export default LoginForm;
