import React from "react";
import Box from "@mui/material/Box";
import Button from "@mui/material/Button";
import SendIcon from "@mui/icons-material/GitHub";
function Footer(props) {
  return (
    <Box>
      <Button
        component="a"
        href="https://github.com/arash-goodarzi/DataScience_HR-Analytics"
        sx={{ display: "flex", alignItems: "center", justifyContent: "center" }}
        endIcon={<SendIcon />}
      >
        GitHub
      </Button>
    </Box>
  );
}

Footer.propTypes = {};

export default Footer;
