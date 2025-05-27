"use client";

import { useEffect } from "react";
import { useFormState } from "react-dom";
import { useRouter } from "next/navigation";
import { Alert, Box, Field, Input, Stack } from "@chakra-ui/react";
import { loginAction, LoginFormState } from "@/actions/login-action";
import LoginButton from "./LoginButton";

const initialState: LoginFormState = {
  success: false,
  message: "",
  errors: {},
};

const LoginForm = () => {
  const [state, formAction] = useFormState(loginAction, initialState);
  const router = useRouter();

  useEffect(() => {
    if (state.success && state.redirectTo) {
      router.push(state.redirectTo);
    }
  }, [state.success, state.redirectTo, router]);

  return (
    <form action={formAction}>
      <Stack gap={4}>
        <Field.Root invalid={!!state.errors?.email}>
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
          {state.errors?.email && (
            <Field.ErrorText>{state.errors.email.join(", ")}</Field.ErrorText>
          )}
        </Field.Root>

        <Field.Root invalid={!!state.errors?.password}>
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
          {state.errors?.password && (
            <Field.ErrorText>
              {state.errors.password.join(", ")}
            </Field.ErrorText>
          )}
        </Field.Root>

        {/* Display general errors from the server action */}
        {state.errors?.general && (
          <Alert.Root status="error" borderRadius="md">
            <Alert.Indicator />
            <Box>
              {state.errors.general.map((errorMsg, index) => (
                <span key={index}>
                  {errorMsg}
                  <br />
                </span>
              ))}
            </Box>
          </Alert.Root>
        )}

        <LoginButton />
      </Stack>
    </form>
  );
};

export default LoginForm;
