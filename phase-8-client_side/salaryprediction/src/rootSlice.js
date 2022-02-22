import { createSlice } from "@reduxjs/toolkit";

export const rootSlice = createSlice({
  name: "valueItemInForm",
  initialState: {
    size: 350,
    consultant: true,
    remoteJob: true,
    rate: 4.5,
    industry: "company_industry_Accounting",
    position: "position_employee",
    sector: "company_sector_biotech & pharmaceuticals",
    title: "title_data analyst",
    skills: ["logstash", "scala"],
  },
  reducers: {
    chooseSize: (state, action) => {
      state.size = action.payload;
    },
    chooseConsultant: (state, action) => {
      state.consultant = action.payload;
    },
    chooseRemoteJob: (state, action) => {
      state.remoteJob = action.payload;
    },
    chooseRate: (state, action) => {
      state.rate = action.payload;
    },
    chooseIndustry: (state, action) => {
      state.industry = action.payload;
    },
    choosePosition: (state, action) => {
      state.position = action.payload;
    },
    chooseSector: (state, action) => {
      state.sector = action.payload;
    },
    chooseTitle: (state, action) => {
      state.title = action.payload;
    },
    chooseToggleSkill: (state, action) => {
      state.skills.includes(action.payload)
        ? state.skills.splice(state.skills.indexOf(action.payload))
        : state.skills.push(action.payload);
    },
  },
});

export default rootSlice.reducer;

export const {
  chooseSize,
  chooseConsultant,
  chooseRemoteJob,
  chooseRate,
  chooseIndustry,
  choosePosition,
  chooseSector,
  chooseTitle,
  chooseToggleSkill,
} = rootSlice.actions;
