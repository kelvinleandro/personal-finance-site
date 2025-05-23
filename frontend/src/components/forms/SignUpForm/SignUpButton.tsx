"use client";

import { Button } from "@chakra-ui/react";
import React from "react";
import { useFormStatus } from "react-dom";

const SignUpButton = () => {
  const { pending } = useFormStatus();

  return (
    <Button
      type="submit"
      bg="black"
      color="white"
      width="full"
      loading={pending}
      loadingText="Signing up..."
    >
      Sign Up
    </Button>
  );
};

export default SignUpButton;
