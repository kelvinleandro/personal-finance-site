"use client";

import { Heading, VStack } from "@chakra-ui/react";
import React from "react";
import { motion } from "framer-motion";

const MotionHeading = motion.create(Heading);

const OurResources = () => {
  return (
    <VStack id="our-resources" as="section">
      <MotionHeading
        as={"h2"}
        size={"4xl"}
        initial={{ opacity: 0, scale: 0 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.5 }}
      >
        Our Resources
      </MotionHeading>

      <Heading as={"h3"} size={"2xl"}>
        Lorem ipsum dolor sit amet consectetur adipisicing elit.
      </Heading>
    </VStack>
  );
};

export default OurResources;
