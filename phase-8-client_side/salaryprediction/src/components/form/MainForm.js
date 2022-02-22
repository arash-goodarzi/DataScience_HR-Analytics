import React, { useEffect, useState } from "react";
import { StyledMainForm } from "./MainForm.styles";
import GeneralQuestion from "./GeneralQuestion";
import SkillsDeails from "./Skills";
import TitleDescription from "./TitleDescription";
import SectorDescription from "./SectorDescription";
import IndustryDescription from "./IndustryDescription";
import SendIcon from "@mui/icons-material/Send";

import { Button } from "@mui/material";

import PositionDescription from "./PositionDescription";

function MainForm(props) {
  const [salaryPredict, setSalaryPredict] = useState("");

  let handleSubmit = async (e) => {
    console.log(props);
    // e.preventDefault();
    // try {
    //   let res = await fetch("https://httpbin.org/post", {
    //     method: "POST",
    //     body: JSON.stringify({
    //       name: name,
    //       email: email,
    //       mobileNumber: mobileNumber,
    //     }),
    //   });
    //   let resJson = await res.json();
    //   if (res.status === 200) {
    //     setName("");
    //     setEmail("");
    //     setMobileNumber("");
    //     setMessage("User created successfully");
    //   } else {
    //     setMessage("Some error occured");
    //   }
    // } catch (err) {
    //   console.log(err);
    // }
  };

  return (
    <StyledMainForm onSubmit={handleSubmit}>
      <fieldset>
        <legend>Job Details</legend>
        <GeneralQuestion></GeneralQuestion>
      </fieldset>
      <fieldset>
        <legend>Skills</legend>
        <SkillsDeails></SkillsDeails>
      </fieldset>
      <fieldset>
        <legend>Industry</legend>
        <IndustryDescription></IndustryDescription>
      </fieldset>
      <fieldset>
        <legend>Sector</legend>
        <SectorDescription />
      </fieldset>
      <fieldset>
        <legend>Title</legend>
        <TitleDescription></TitleDescription>
      </fieldset>
      <fieldset>
        <legend>Position</legend>
        <PositionDescription></PositionDescription>
      </fieldset>
      <Button variant="contained" type="submit" endIcon={<SendIcon />}>
        Predict
      </Button>
    </StyledMainForm>
  );
}

export default MainForm;
// https://mui.com/getting-started/usage/
