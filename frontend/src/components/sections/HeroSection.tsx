import { Flex, Box, Text } from "@chakra-ui/react";

const HeroSection = () => {
  return (
    <Flex id="hero">
      <Box>
        <Text fontWeight="bold" fontSize="4xl">
          Bem vindo ao <Text as="span">SEM TITULO</Text>
        </Text>

        <Text fontWeight="semibold" fontSize="xl">
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
        </Text>
      </Box>
    </Flex>
  );
};

export default HeroSection;
