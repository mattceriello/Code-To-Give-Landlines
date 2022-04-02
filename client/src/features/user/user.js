import { createSlice } from "@reduxjs/toolkit";

const initialValue = null;
export const userSlice = createSlice({
  name: "user",
  initialState: { value: initialValue },
  reducers: {
    setCredentials: (state, action) => {
      state.value = action.payload;
    },
    logout: (state) => {
      state.value = initialValue;
    },
  },
});

export const { setCredentials, logout } = userSlice.actions;

export default userSlice.reducer;
