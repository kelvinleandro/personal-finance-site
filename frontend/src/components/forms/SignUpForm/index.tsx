"use client";

import { Field, Fieldset, Input, SimpleGrid, Stack } from "@chakra-ui/react";
import SignUpButton from "./SignUpButton";
import { signupAction } from "@/actions/signup-action";

const SignUpForm = () => {
  const inputProps = {
    color: "black",
    _placeholder: { color: "gray.500" },
    px: 2,
  };

  const handleFormAction = async (formData: FormData) => {
    try {
      await signupAction(formData);
    } catch (error) {
      alert(error);
    }
  };

  return (
    <form action={handleFormAction}>
      <Stack gap={6}>
        {/* Personal Info */}
        <Fieldset.Root>
          <Fieldset.Legend fontWeight="semibold" color="black" fontSize="lg">
            Personal Info
          </Fieldset.Legend>
          <Fieldset.Content>
            <SimpleGrid columns={{ base: 1, md: 2 }} gap={4}>
              <Field.Root>
                <Field.Label color="black">First Name</Field.Label>
                <Input
                  {...inputProps}
                  name="first_name"
                  required
                  placeholder="Enter your first name"
                />
              </Field.Root>
              <Field.Root>
                <Field.Label color="black">Last Name</Field.Label>
                <Input
                  {...inputProps}
                  name="last_name"
                  required
                  placeholder="Enter your last name"
                />
              </Field.Root>
              <Field.Root>
                <Field.Label color="black">CPF</Field.Label>
                <Input
                  {...inputProps}
                  name="cpf"
                  required
                  placeholder="Enter your CPF"
                />
              </Field.Root>
              <Field.Root>
                <Field.Label color="black">Birth Date</Field.Label>
                <Input {...inputProps} type="date" name="birth_date" required />
              </Field.Root>
            </SimpleGrid>

            <Field.Root>
              <Field.Label color="black">Email</Field.Label>
              <Input
                {...inputProps}
                type="email"
                name="email"
                required
                placeholder="Enter your email"
              />
            </Field.Root>

            <Field.Root>
              <Field.Label color="black">Password</Field.Label>
              <Input
                {...inputProps}
                type="password"
                name="password"
                required
                placeholder="Enter your password"
              />
            </Field.Root>

            <Field.Root>
              <Field.Label color="black">Phone Number</Field.Label>
              <Input
                {...inputProps}
                name="phone_numbers[0].number"
                required
                placeholder="Enter your phone number"
              />
            </Field.Root>
          </Fieldset.Content>
        </Fieldset.Root>

        {/* Address Info */}
        <Fieldset.Root>
          <Fieldset.Legend fontWeight="semibold" color="black" fontSize="lg">
            Address
          </Fieldset.Legend>
          <Fieldset.Content>
            <SimpleGrid columns={{ base: 1, md: 2 }} gap={4}>
              <Field.Root>
                <Field.Label color="black">ZIP Code</Field.Label>
                <Input
                  {...inputProps}
                  name="zip_code"
                  required
                  placeholder="Enter your ZIP code"
                />
              </Field.Root>
              <Field.Root>
                <Field.Label color="black">Street</Field.Label>
                <Input
                  {...inputProps}
                  name="street"
                  required
                  placeholder="Enter your street"
                />
              </Field.Root>
            </SimpleGrid>

            <SimpleGrid columns={{ base: 1, md: 2 }} gap={4}>
              <Field.Root>
                <Field.Label color="black">Number</Field.Label>
                <Input
                  {...inputProps}
                  name="number"
                  required
                  placeholder="Enter your house number"
                />
              </Field.Root>
              <Field.Root>
                <Field.Label color="black">Complement</Field.Label>
                <Input
                  {...inputProps}
                  name="complement"
                  placeholder="Apt, suite, etc. (optional)"
                />
              </Field.Root>
            </SimpleGrid>

            <Field.Root>
              <Field.Label color="black">Neighborhood</Field.Label>
              <Input
                {...inputProps}
                name="neighborhood"
                required
                placeholder="Enter your neighborhood"
              />
            </Field.Root>

            <SimpleGrid columns={{ base: 1, md: 2 }} gap={4}>
              <Field.Root>
                <Field.Label color="black">City</Field.Label>
                <Input
                  {...inputProps}
                  name="city"
                  required
                  placeholder="Enter your city"
                />
              </Field.Root>
              <Field.Root>
                <Field.Label color="black">State</Field.Label>
                <Input
                  {...inputProps}
                  name="state"
                  required
                  placeholder="Enter your state"
                />
              </Field.Root>
            </SimpleGrid>
          </Fieldset.Content>
        </Fieldset.Root>

        <SignUpButton />
      </Stack>
    </form>
  );
};

export default SignUpForm;
