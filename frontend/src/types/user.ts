export interface UserCredentials {
  email: string;
  password: string;
}

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
