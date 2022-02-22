import React from "react";
import { StyledNav } from "./Nav.styles";
import List from "@mui/material/List";
import ListItem from "@mui/material/ListItem";
import ListItemButton from "@mui/material/ListItemButton";
import ListItemIcon from "@mui/material/ListItemIcon";
import ListItemText from "@mui/material/ListItemText";
import Filter1RoundedIcon from "@mui/icons-material/Filter1Rounded";
import Filter2RoundedIcon from "@mui/icons-material/Filter2Rounded";
import Filter3RoundedIcon from "@mui/icons-material/Filter3Rounded";
import Filter4RoundedIcon from "@mui/icons-material/Filter4Rounded";
import Filter5RoundedIcon from "@mui/icons-material/Filter5Rounded";
import Filter6RoundedIcon from "@mui/icons-material/Filter6Rounded";
import Filter7RoundedIcon from "@mui/icons-material/Filter7Rounded";
import Filter8RoundedIcon from "@mui/icons-material/Filter8Rounded";
import ViewListRoundedIcon from "@mui/icons-material/ViewListRounded";
import { useEffect, useState } from "react";
import axios from "axios";

const api = axios.create({ baseURL: `http://127.0.0.1:5000/` });

// useEffect(() => {
//   const fetchPosts = async () => {
//     try {
//       const response = await api.get("/api");
//       console.log(response);
//     } catch (err) {
//       console.log(err.data);
//       console.log(err.status);
//       console.log(err.headers);
//     }
//   };
// }, []);

function Nav(props) {
  // console.log("------------------------------------");
  // useEffect(() => {
  //   fetch("/api")
  //     .then((res) => {
  //       if (res.ok) {
  //         console.log("1111");
  //         console.log(res);
  //         console.log("9090");
  //         return res.json();
  //       }
  //     })
  //     .then((jsonResponse) => {
  //       console.log("==>");
  //       console.log(jsonResponse);
  //     });
  // }, []);

  return (
    <StyledNav>
      <List>
        <ListItem>
          <ListItemButton
            component="a"
            href="https://github.com/arash-goodarzi/DataScience_HR-Analytics"
          >
            <ListItemIcon>
              <ViewListRoundedIcon />
            </ListItemIcon>
            <ListItemText primary="Steps" />
          </ListItemButton>
        </ListItem>
        <ListItem>
          <ListItemButton
            component="a"
            href="https://github.com/arash-goodarzi/DataScience_HR-Analytics/blob/master/phase-1-scraping-glassdoor.py"
          >
            <ListItemIcon>
              <Filter1RoundedIcon />
            </ListItemIcon>
            <ListItemText primary="Data Collection" />
          </ListItemButton>
        </ListItem>
        <ListItem>
          <ListItemButton
            component="a"
            href="https://github.com/arash-goodarzi/DataScience_HR-Analytics/blob/master/phase-2-integrated-data.py"
          >
            <ListItemIcon>
              <Filter2RoundedIcon />
            </ListItemIcon>
            <ListItemText primary="Integrate Data" />
          </ListItemButton>
        </ListItem>
        <ListItem>
          <ListItemButton
            component="a"
            href="https://github.com/arash-goodarzi/DataScience_HR-Analytics/blob/master/phase-3-Clean-data.py"
          >
            <ListItemIcon>
              <Filter3RoundedIcon />
            </ListItemIcon>
            <ListItemText primary="Data Cleaning" />
          </ListItemButton>
        </ListItem>
        <ListItem>
          <ListItemButton
            component="a"
            href="https://github.com/arash-goodarzi/DataScience_HR-Analytics/blob/master/phase-4-Enrich-data.py"
          >
            <ListItemIcon>
              <Filter4RoundedIcon />
            </ListItemIcon>
            <ListItemText primary="Extract data" />
          </ListItemButton>
        </ListItem>
        <ListItem>
          <ListItemButton
            component="a"
            href="https://github.com/arash-goodarzi/DataScience_HR-Analytics/blob/master/phase-5-EDA-Exploratory%20Data%20analysis.ipynb"
          >
            <ListItemIcon>
              <Filter5RoundedIcon />
            </ListItemIcon>
            <ListItemText primary="Exploratory Data analysis" />
          </ListItemButton>
        </ListItem>
        <ListItem>
          <ListItemButton
            component="a"
            href="https://github.com/arash-goodarzi/DataScience_HR-Analytics/blob/master/phase-6-model_building.py"
          >
            <ListItemIcon>
              <Filter6RoundedIcon />
            </ListItemIcon>
            <ListItemText primary="Building of Model" />
          </ListItemButton>
        </ListItem>
        <ListItem>
          <ListItemButton
            component="a"
            href="https://github.com/arash-goodarzi/DataScience_HR-Analytics/tree/master/flaskAPI"
          >
            <ListItemIcon>
              <Filter7RoundedIcon />
            </ListItemIcon>
            <ListItemText primary="Server side via Flask" />
          </ListItemButton>
        </ListItem>
        <ListItem>
          <ListItemButton component="a" href="#simple-list">
            <ListItemIcon>
              <Filter8RoundedIcon />
            </ListItemIcon>
            <ListItemText primary="Client side via React" />
          </ListItemButton>
        </ListItem>
      </List>
    </StyledNav>
  );
}

export default Nav;
