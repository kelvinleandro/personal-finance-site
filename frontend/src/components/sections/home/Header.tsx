import { Flex, HStack, Button, Text } from "@chakra-ui/react";
import React from "react";

const Header = () => {
  return (
    <Flex as={"header"} justify="space-between" align="center" px={4} py={2}>
      <Text>Logo</Text>

      <HStack>
        <Button variant="ghost" px={2}>
          Sobre
        </Button>
        <Button variant="ghost" px={2}>
          Recursos
        </Button>
        <Button variant="subtle" px={2}>
          Log In
        </Button>
        <Button px={2}>Sign Up</Button>
      </HStack>
    </Flex>
  );
};

export default Header;
