import { Box, Center, Text } from "@chakra-ui/react";
import Link from "next/link";
import LoginForm from "@/components/forms/LoginForm";

const LoginPage = () => {
  return (
    <Center w="100%" h="100vh">
      <Box p={4} bg="gray.300" w={{ base: "80%", md: "50%" }}>
        <Text textAlign="center" fontSize="2xl" fontWeight="bold" color="black">
          Login
        </Text>

        <LoginForm />

        <Link href="/signup">
          <Text color="blue.700" _hover={{ textDecoration: "underline" }}>
            Don&apos;t you have an account? Sign up
          </Text>
        </Link>
      </Box>
    </Center>
  );
};

export default LoginPage;
