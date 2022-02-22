import React from "react";
import { RadioGroup, Radio, FormControlLabel } from "@mui/material";

import { useSelector, useDispatch } from "react-redux";

import { chooseTitle } from "../../rootSlice";

function TitleDescription(props) {
  const {} = props;
  const titles = [
    { title: "title_data analyst", desc: "data analyst" },
    { title: "title_data architect", desc: "data architect" },
    { title: "title_data engineer", desc: "data engineer" },
    { title: "title_data scientist", desc: "data scientist" },
    { title: "title_machine learning", desc: "machine learning" },
    {
      title: "title_machine learning engineer",
      desc: "machine learning engineer",
    },
    { title: "title_statistician", desc: "statistician" },
  ];

  const [value, setValue] = React.useState("job_title");
  const handleChange = (event) => {
    setValue(event.target.value);
  };

  const dispatch = useDispatch();
  const title_redux = useSelector((state) => state.valueItemInForm.title);

  return (
    <RadioGroup
      aria-labelledby="demo-controlled-radio-buttons-group"
      name="controlled-radio-buttons-group"
      value={title_redux}
      onChange={(e) => {
        dispatch(chooseTitle(e.target.value));
      }}
      row
    >
      {titles.map((tlt, i) => (
        <FormControlLabel
          value={tlt.title}
          control={<Radio />}
          key={i}
          label={tlt.desc}
        />
      ))}
    </RadioGroup>
  );
}

export default TitleDescription;
