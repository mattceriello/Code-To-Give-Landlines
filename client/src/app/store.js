import { configureStore } from "@reduxjs/toolkit";
import userReducer from "../features/user/user";
import { authApi } from "../services/userApi";
export default configureStore({
  reducer: {
    [authApi.reducerPath]: authApi.reducer,
    user: userReducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(authApi.middleware),
});
