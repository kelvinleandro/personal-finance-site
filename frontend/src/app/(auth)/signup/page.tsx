import { Box, Center, Text } from "@chakra-ui/react";
import Link from "next/link";
import SignUpForm from "@/components/forms/SignUpForm";

const SignUpPage = () => {
  return (
    <Center w="100%" h="100%" py={8}>
      <Box p={4} bg="gray.300" w={{ base: "80%", md: "50%" }}>
        <Text textAlign="center" fontSize="2xl" fontWeight="bold" color="black">
          Sign Up
        </Text>

        <SignUpForm />

        <Link href="/login">
          <Text color="blue.700" _hover={{ textDecoration: "underline" }}>
            Already have an account? Login.
          </Text>
        </Link>
      </Box>
    </Center>
  );
};

export default SignUpPage;
