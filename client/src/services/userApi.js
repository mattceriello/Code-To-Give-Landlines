import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

const baseUrl = "https://code-to-give-mavericks.herokuapp.com";

export const authApi = createApi({
  reducerPath: "authApi",
  baseQuery: fetchBaseQuery({ baseUrl }),
  endpoints: (builder) => ({
    login: builder.mutation({
      query: (credentials) => {
        return {
          url: "/login",
          method: "post",
          body: credentials,
        };
      },
    }),
    register: builder.mutation({
      query: (credentials) => {
        return {
          url: "/register",
          method: "post",
          body: credentials,
        };
      },
    }),
  }),
});

export const { useLoginMutation, useRegisterMutation } = authApi;
