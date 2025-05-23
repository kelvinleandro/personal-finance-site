import { Token } from "@/types/token";
import { cookies } from "next/headers";

export async function saveTokens(tokens: Partial<Token>) {
  const cookieStore = await cookies();

  if (tokens.access)
    cookieStore.set("access", tokens.access, { httpOnly: true });
  if (tokens.refresh)
    cookieStore.set("refresh", tokens.refresh, { httpOnly: true });
}

export async function deleteTokens() {
  const cookieStore = await cookies();
  cookieStore.delete("access");
  cookieStore.delete("refresh");
}
