import { z } from "zod";

export const LoginSchema = z.object({
  email: z.string().email({ message: "Invalid email address." }),
  password: z.string().min(1, { message: "Password cannot be empty." }),
});

export type LoginCredentials = z.infer<typeof LoginSchema>;

export interface PhoneNumber {
  id?: number;
  number: string;
  type?: string;
}

export interface Address {
  street: string;
  number: string;
  complement: string;
  neighborhood: string;
  city: string;
  state: string;
  zip_code: string;
}

export interface UserPersonalInfo extends Address {
  cpf: string;
  first_name: string;
  last_name: string;
  birth_date: string;
  email: string;
  password: string;
  phone_numbers: PhoneNumber[];
}
