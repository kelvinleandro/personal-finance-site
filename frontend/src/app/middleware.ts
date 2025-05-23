import { NextRequest, NextResponse } from "next/server";

export function middleware(request: NextRequest) {
  const access = request.cookies.get("access")?.value;
  const pathname = request.nextUrl.pathname;

  const isAuthenticated = !!access;

  const isProtected = pathname.startsWith("/(protected)");
  const isPublicAuth = pathname.startsWith("/(auth)");

  if (isProtected && !isAuthenticated) {
    return NextResponse.redirect(new URL("/(auth)/login", request.url));
  }

  if (isPublicAuth && isAuthenticated) {
    return NextResponse.redirect(
      new URL("/(protected)/dashboard", request.url)
    );
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/(auth)/:path*", "/(protected)/:path*"],
};
