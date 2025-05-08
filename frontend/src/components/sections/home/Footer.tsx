import React from "react";
import { Flex, Link, Stack, Text } from "@chakra-ui/react";

const Footer = () => {
  return (
    <Flex
      as="footer"
      direction={{ base: "column", md: "row" }}
      align="center"
      justify={{ base: "center", md: "space-between" }}
    >
      <Text>@ Copyright 2025. Todos os direitos reservados.</Text>

      <Stack direction={{ base: "column", md: "row" }}>
        <Link href="#">Políticas de privacidade</Link>
        <Link href="#">Termos e condições</Link>
      </Stack>
    </Flex>
  );
};

export default Footer;
