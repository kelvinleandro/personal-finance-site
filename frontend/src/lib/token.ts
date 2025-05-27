import { Token } from "@/types/token";
import { cookies } from "next/headers";

const ACCESS_TOKEN_MAX_AGE = 60 * 15;
const REFRESH_TOKEN_MAX_AGE = 60 * 60 * 24 * 7;

export async function saveTokens(tokens: Partial<Token>) {
  const cookieStore = await cookies();

  const commonOptions = {
    httpOnly: true,
    secure: process.env.NODE_ENV === "production",
    path: "/",
    sameSite: "lax" as const,
  };

  if (tokens.access) {
    cookieStore.set("access", tokens.access, {
      ...commonOptions,
      maxAge: ACCESS_TOKEN_MAX_AGE,
    });
  }
  if (tokens.refresh) {
    cookieStore.set("refresh", tokens.refresh, {
      ...commonOptions,
      maxAge: REFRESH_TOKEN_MAX_AGE,
    });
  }
}

export async function getAccessToken() {
  const cookieStore = await cookies();
  return cookieStore.get("access")?.value;
}

export async function getRefreshToken() {
  const cookieStore = await cookies();
  return cookieStore.get("refresh")?.value;
}

export async function clearTokens() {
  const cookieStore = await cookies();
  cookieStore.set("access", "", { path: "/", httpOnly: true, maxAge: 0 });
  cookieStore.set("refresh", "", { path: "/", httpOnly: true, maxAge: 0 });
  // cookieStore.delete("access");
  // cookieStore.delete("refresh");
}
