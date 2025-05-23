"use client";

import { Button } from "@chakra-ui/react";
import React from "react";
import { useFormStatus } from "react-dom";

const LoginButton = () => {
  const { pending } = useFormStatus();

  return (
    <Button
      type="submit"
      bg="black"
      color="white"
      width="full"
      loading={pending}
      loadingText="Logging in..."
    >
      Login
    </Button>
  );
};

export default LoginButton;
