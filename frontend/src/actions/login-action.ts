"use server";

import { loginUser } from "@/services/auth";
import { saveTokens } from "@/lib/token";

export async function loginAction(formData: FormData) {
  const email = formData.get("email") as string;
  const password = formData.get("password") as string;

  const tokens = await loginUser({ email, password });

  await saveTokens(tokens);
}
