import { Box, Button, HStack, Flex, Text } from "@chakra-ui/react";
import HeroSection from "@/components/sections/HeroSection";
import Footer from "@/components/sections/Footer";

export default function Home() {
  return (
    <Box>
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

      <HeroSection />

      <Footer />
    </Box>
  );
}
