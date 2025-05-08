"use client";

import { Testimonial } from "@/types/testimonials";
import { Box, VStack, Flex, Text, useBreakpointValue } from "@chakra-ui/react";
import { useState, useEffect } from "react";
import { motion, AnimatePresence } from "framer-motion";

const TestimonialCard = ({ name, text }: Omit<Testimonial, "id">) => (
  <Box
    bg="white"
    boxShadow="md"
    borderRadius="lg"
    p={6}
    minW={{ base: "280px", md: "300px" }}
    maxW={{ base: "280px", md: "300px" }}
    mx={2}
  >
    <VStack align="start" gap={4}>
      <Text fontSize="md" color="gray.600">
        &quot;{text}&quot;
      </Text>
      <Text fontWeight="bold" color="gray.800">
        - {name}
      </Text>
    </VStack>
  </Box>
);

const TestimonialSlider = ({
  testimonials,
}: {
  testimonials: Testimonial[];
}) => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isPaused, setIsPaused] = useState(false);

  const slidesToShow = useBreakpointValue({ base: 1, md: 3 });
  const isMobile = slidesToShow === 1;

  useEffect(() => {
    if (!isPaused) {
      const interval = setInterval(() => {
        setCurrentIndex((prevIndex) =>
          prevIndex >= testimonials.length - slidesToShow! ? 0 : prevIndex + 1
        );
      }, 2000);
      return () => clearInterval(interval);
    }
  }, [isPaused, slidesToShow, testimonials.length]);

  const getVisibleTestimonials = () => {
    const visible = [];
    for (let i = 0; i < slidesToShow!; i++) {
      const index = (currentIndex + i) % testimonials.length;
      visible.push(testimonials[index]);
    }
    return visible;
  };

  return (
    <Box
      py={4}
      onMouseEnter={() => setIsPaused(true)}
      onMouseLeave={() => setIsPaused(false)}
    >
      <Flex
        overflow="hidden"
        justify="center"
        align="center"
        position="relative"
        direction="row"
      >
        <AnimatePresence initial={false}>
          <motion.div
            key={currentIndex}
            initial={{ x: isMobile ? 300 : 900, opacity: 0 }}
            animate={{ x: 0, opacity: 1 }}
            exit={{ x: isMobile ? -300 : -900, opacity: 0 }}
            transition={{ duration: 0.5 }}
            style={{ display: "flex", flexDirection: "row" }}
          >
            {getVisibleTestimonials().map((testimonial, index) => (
              <TestimonialCard
                key={`${testimonial.id}-${index}`}
                name={testimonial.name}
                text={testimonial.text}
              />
            ))}
          </motion.div>
        </AnimatePresence>
      </Flex>
    </Box>
  );
};

export default TestimonialSlider;
