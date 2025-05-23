import { Flex, HStack, Button, Text } from "@chakra-ui/react";
import React from "react";
import Link from "next/link";

const Header = () => {
  return (
    <Flex as={"header"} justify="space-between" align="center" px={4} py={2}>
      <Text asChild>
        <a href="">Logo</a>
      </Text>

      <HStack>
        <Link href="#">
          <Button variant="ghost" px={2}>
            About
          </Button>
        </Link>
        <Link href="#our-resources">
          <Button variant="ghost" px={2}>
            Resources
          </Button>
        </Link>
        <Link href="/login">
          <Button variant="subtle" px={2}>
            Log In
          </Button>
        </Link>
        <Link href="/signup">
          <Button px={2}>Sign Up</Button>
        </Link>
      </HStack>
    </Flex>
  );
};

export default Header;
