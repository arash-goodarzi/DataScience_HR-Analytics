import React from "react";
import { StyledTitle } from "./Title.styles";
import { StyledTitleImage } from "./TitleImage.styles";

const Title = (props) => {
  return (
    <StyledTitle>
      <StyledTitleImage src="./images/header.jpg" />
    </StyledTitle>
  );
};

export default Title;
