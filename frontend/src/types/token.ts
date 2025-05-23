export type Token = {
  access: string;
  refresh: string;
};

export type RefreshToken = Omit<Token, "access">;

export type AccessToken = Omit<Token, "refresh">;
