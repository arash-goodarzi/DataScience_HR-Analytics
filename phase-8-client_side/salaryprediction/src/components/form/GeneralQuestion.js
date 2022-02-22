import React from "react";
import {
  Slider,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Box,
  Grid,
} from "@mui/material";

import { useSelector, useDispatch } from "react-redux";

import {
  chooseSize,
  chooseConsultant,
  chooseRemoteJob,
  chooseRate,
} from "../../rootSlice";

function GeneralQuestion() {
  const company_sizes = [
    { comany_size: "1 to 50 Employees", value: 25 },
    { comany_size: "51 to 200 Employees", value: 100 },
    { comany_size: "201 to 500 Employees", value: 350 },
    { comany_size: "501 to 1000 Employees", value: 750 },
    { comany_size: "1001 to 5000 Employees", value: 3000 },
    { comany_size: "5001 to 10000 Employees", value: 7500 },
    { comany_size: "10000+ Employee", value: 10000 },
  ];

  const size_redux = useSelector((state) => state.valueItemInForm.size);
  const consultant_redux = useSelector(
    (state) => state.valueItemInForm.consultant
  );
  const remoteJob_redux = useSelector(
    (state) => state.valueItemInForm.remoteJob
  );
  const rate_redux = useSelector((state) => state.valueItemInForm.rate);

  const dispatch = useDispatch();

  return (
    <Grid container>
      <Grid item xs={3}>
        <FormControl>
          <InputLabel>Company Size</InputLabel>
          <Select
            value={size_redux}
            name="avg_employees"
            onChange={(e) => {
              dispatch(chooseSize(e.target.value));
            }}
            id="demo-simple-select"
          >
            {company_sizes.map((sz, i) => (
              <MenuItem value={sz.value} key={i}>
                {sz.comany_size}
              </MenuItem>
            ))}
          </Select>
        </FormControl>
      </Grid>
      <Grid item xs={3}>
        <FormControl>
          <InputLabel>Consultant</InputLabel>
          <Select
            value={consultant_redux}
            name="per_hour"
            onChange={(e) => {
              dispatch(chooseConsultant(e.target.value));
            }}
          >
            <MenuItem value="true">Consultant</MenuItem>
            <MenuItem value="false">Employee</MenuItem>
          </Select>
        </FormControl>
      </Grid>
      <Grid item xs={3}>
        <FormControl>
          <InputLabel>Remote Job</InputLabel>
          <Select
            value={remoteJob_redux}
            name="remote_work"
            onChange={(e) => {
              dispatch(chooseRemoteJob(e.target.value));
            }}
          >
            <MenuItem value="false">Office job</MenuItem>
            <MenuItem value="true">Remote job</MenuItem>
          </Select>
        </FormControl>
      </Grid>
      <Grid item xs={3}>
        <FormControl>
          <InputLabel>Company Ranking</InputLabel>
          <Box width={200}>
            <Slider
              min={0}
              max={5}
              value={rate_redux}
              step={0.1}
              onChange={(e) => {
                dispatch(chooseRate(e.target.value));
              }}
              aria-label="Default"
              valueLabelDisplay="auto"
              color="primary"
            />
          </Box>
        </FormControl>
      </Grid>
    </Grid>
  );
}

export default GeneralQuestion;
