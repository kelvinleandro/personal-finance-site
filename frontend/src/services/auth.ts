import api from "@/lib/api";
import { Token } from "@/types/token";
import { UserCredentials } from "@/types/user";

export async function loginUser(userData: UserCredentials): Promise<Token> {
  const response = await api.post("/auth/login", userData);
  return response.data;
}

export async function signupUser(userData: object) {
  const response = await api.post("/auth/signup", userData);
  return response.data;
}
