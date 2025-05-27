"use server";

import { loginUser } from "@/services/auth";
import { saveTokens } from "@/lib/token";
import { LoginSchema } from "@/types/user";
import { isAxiosError } from "axios";

export interface LoginFormState {
  success: boolean;
  message?: string;
  errors?: {
    email?: string[];
    password?: string[];
    general?: string[];
  };
  redirectTo?: string;
}

export async function loginAction(
  prevState: LoginFormState,
  formData: FormData
): Promise<LoginFormState> {
  const formValues = Object.fromEntries(formData.entries());

  // 1. Validate input (using Zod as an example)
  const validationResult = LoginSchema.safeParse(formValues);
  if (!validationResult.success) {
    // Map Zod errors to your LoginFormState.errors structure
    const fieldErrors: LoginFormState["errors"] = {};
    for (const issue of validationResult.error.issues) {
      if (issue.path.length > 0) {
        const field = issue.path[0] as keyof typeof fieldErrors;
        if (!fieldErrors[field]) {
          fieldErrors[field] = [];
        }
        (fieldErrors[field] as string[]).push(issue.message);
      } else {
        if (!fieldErrors.general) fieldErrors.general = [];
        fieldErrors.general.push(issue.message);
      }
    }
    return {
      success: false,
      message: "Invalid input. Please check the fields.",
      errors: fieldErrors,
    };
  }

  try {
    const tokens = await loginUser(validationResult.data);
    await saveTokens(tokens);
    // Important: After successful login and token saving, trigger a redirect from the action
    // However, redirect() must be called outside of a try/catch block.
    // So, we set a state for redirection.
    // For direct redirect, you'd call redirect('/(protected)/dashboard') here,
    // but useFormState works better by returning a state.
    // The component can then use router.push or window.location based on this state.
    return {
      success: true,
      message: "Login successful!",
      redirectTo: "/dashboard", // Or your desired redirect path
    };
  } catch (error: unknown) {
    console.error("Login action error:", error);
    const errorMessage = "Login failed. Please try again.";
    const errors: LoginFormState["errors"] = { general: [] };

    if (isAxiosError(error)) {
      // Type guard for Axios errors
      if (error.response && error.response.data) {
        const backendErrors = error.response.data;
        // Example: Django REST Framework often returns errors like:
        // { "detail": "No active account found..." }
        // Or for field-specific: { "email": ["Enter a valid email address."], "non_field_errors": ["Unable to log in..."] }
        if (typeof backendErrors === "object" && backendErrors !== null) {
          if (backendErrors.detail) {
            (errors.general as string[]).push(backendErrors.detail);
          }
          if (backendErrors.non_field_errors) {
            (errors.general as string[]).push(
              ...(Array.isArray(backendErrors.non_field_errors)
                ? backendErrors.non_field_errors
                : [backendErrors.non_field_errors])
            );
          }
          // If Django returns field-specific errors not under "detail" or "non_field_errors"
          // you might map them here, e.g., if backendErrors.email:
          if (backendErrors.email && Array.isArray(backendErrors.email)) {
            errors.email = backendErrors.email;
          }
          if (backendErrors.password && Array.isArray(backendErrors.password)) {
            errors.password = backendErrors.password;
          }

          // If no specific error messages were pushed, use the generic one.
          if (
            (errors.general as string[]).length === 0 &&
            !errors.email &&
            !errors.password
          ) {
            (errors.general as string[]).push(errorMessage);
          }
        } else if (typeof backendErrors === "string") {
          (errors.general as string[]).push(backendErrors);
        } else {
          (errors.general as string[]).push(errorMessage);
        }
      } else if (error.request) {
        (errors.general as string[]).push(
          "Network error. Could not connect to the server."
        );
      } else {
        (errors.general as string[]).push(errorMessage);
      }
    } else if (error instanceof Error) {
      // Standard JavaScript Error
      (errors.general as string[]).push(error.message || errorMessage);
    } else {
      // Fallback for other unknown error types
      (errors.general as string[]).push(errorMessage);
    }

    return {
      success: false,
      message:
        errors.general && (errors.general as string[]).length > 0
          ? (errors.general as string[]).join(" ")
          : errorMessage,
      errors: errors,
    };
  }
}
