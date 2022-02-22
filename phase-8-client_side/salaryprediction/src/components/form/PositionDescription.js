import React from "react";
import {
  Radio,
  RadioGroup,
  FormControl,
  FormControlLabel,
} from "@mui/material";

import { useSelector, useDispatch } from "react-redux";

import { choosePosition } from "../../rootSlice";

function PositionDescription(props) {
  const positions = [
    { position: "position_co-op", desc: "position_co-op" },
    { position: "position_consultant", desc: "position_consultant" },
    { position: "position_employee", desc: "position_employee" },
    { position: "position_lead", desc: "position_lead" },
    { position: "position_manager", desc: "position_manager" },
    { position: "position_senior", desc: "position_senior" },
  ];

  const [value, setValue] = React.useState("company_sector");
  const handleChange = (event) => {
    setValue(event.target.value);
  };

  const dispatch = useDispatch();
  const position_redux = useSelector((state) => state.valueItemInForm.position);

  return (
    <FormControl>
      <RadioGroup
        aria-labelledby="demo-controlled-radio-buttons-group"
        name="controlled-radio-buttons-group"
        value={position_redux}
        onChange={(e) => {
          dispatch(choosePosition(e.target.value));
        }}
        row
      >
        {positions.map((pz, i) => (
          <FormControlLabel
            value={pz.position}
            control={<Radio />}
            key={i}
            label={pz.desc}
          />
        ))}
      </RadioGroup>
    </FormControl>
  );
}

export default PositionDescription;
