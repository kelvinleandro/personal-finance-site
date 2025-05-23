"use client";

import { Flex, Box, Text, Button } from "@chakra-ui/react";
import { motion } from "framer-motion";

const MotionBox = motion.create(Box);

const HeroSection = () => {
  return (
    <Flex
      id="hero"
      as={"section"}
      px={16}
      py={8}
      justify={{ base: "center", md: "space-between" }}
      align={{ base: "center", md: "flex-start" }}
      direction={{ base: "column", md: "row" }}
    >
      <MotionBox
        initial={{ opacity: 0, scale: 1.2 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.5 }}
      >
        <Text fontWeight="bold" fontSize="4xl">
          Lorem Ipsum <Text as="span">TRALALERO TRALALA</Text>
        </Text>

        <Text fontWeight="semibold" fontSize="xl">
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
        </Text>

        <Button>Lorem Ipsum</Button>
      </MotionBox>

      <MotionBox
        w={300}
        h={300}
        bg="white"
        initial={{ opacity: 0, x: "+100vw" }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ duration: 0.5 }}
      />
    </Flex>
  );
};

export default HeroSection;
