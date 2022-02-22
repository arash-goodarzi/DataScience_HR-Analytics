import { configureStore } from "@reduxjs/toolkit";
import itemsInForm from "./rootSlice";
import thunk from "redux-thunk";

export const store = configureStore({
  reducer: {
    valueItemInForm: itemsInForm,
  },
});
