import React from "react";
import { StyledProjectId } from "./ProjectId.styles";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";

function ProjectId(props) {
  return (
    <StyledProjectId>
      <List>
        <ListItem>Project Name: Salary Prediction</ListItem>
        <ListItem>Type: End to End Project</ListItem>
        <ListItem>Domain: Data Science</ListItem>
      </List>
    </StyledProjectId>
  );
}

ProjectId.propTypes = {};

export default ProjectId;
