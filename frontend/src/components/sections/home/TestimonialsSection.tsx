import TestimonialSlider from "@/components/TestimonialSlider";
import { getTestimonials } from "@/lib/testimonials";
import { Heading, VStack } from "@chakra-ui/react";
import React from "react";

const TestimonialsSection = () => {
  const testimonials = getTestimonials();

  return (
    <VStack id="testimonials" as="section" width={"100%"}>
      <Heading as={"h2"} size={"4xl"}>
        What our clients say
      </Heading>

      <TestimonialSlider testimonials={testimonials} />
    </VStack>
  );
};

export default TestimonialsSection;
