import { Box } from "@chakra-ui/react";
import HeroSection from "@/components/sections/home/HeroSection";
import Footer from "@/components/sections/home/Footer";
import Header from "@/components/sections/home/Header";
import OurResources from "@/components/sections/home/OurResources";
import TestimonialsSection from "@/components/sections/home/TestimonialsSection";

export default function Home() {
  return (
    <Box>
      <Header />

      <HeroSection />

      <OurResources />

      <TestimonialsSection />

      <Footer />
    </Box>
  );
}
