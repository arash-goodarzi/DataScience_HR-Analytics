import React from "react";
import {
  Radio,
  RadioGroup,
  FormControl,
  FormControlLabel,
} from "@mui/material";

import { useSelector, useDispatch } from "react-redux";

import { chooseSector } from "../../rootSlice";

function SectorDescription(props) {
  const sectors = [
    { sector: "company_type_Accounting", desc: "Accounting" },
    {
      sector: "company_type_Advertising & Marketing",
      desc: "Advertising & Marketing",
    },
    {
      sector: "company_type_College / University",
      desc: "College / University",
    },
    {
      sector: "company_type_Colleges & Universities",
      desc: "Colleges & Universities",
    },
    {
      sector: "company_type_Company - Private",
      desc: "Company - Private",
    },
    {
      sector: "company_type_Company - Public",
      desc: "Company - Public",
    },
    {
      sector: "company_type_Computer Hardware & Software",
      desc: "Computer Hardware & Software",
    },
    { sector: "company_type_Consulting", desc: "Consulting" },
    {
      sector: "company_type_Federal Agencies",
      desc: "Federal Agencies",
    },
    { sector: "company_type_Government", desc: "Government" },
    {
      sector: "company_type_Health Care Services & Hospitals",
      desc: "Health Care Services & Hospitals",
    },
    { sector: "company_type_IT Services", desc: "IT Services" },
    {
      sector: "company_type_Municipal Governments",
      desc: "Municipal Governments",
    },
    {
      sector: "company_type_Nonprofit Organization",
      desc: "Nonprofit Organization",
    },
    {
      sector: "company_type_Private Practice / Firm",
      desc: "Private Practice / Firm",
    },
    {
      sector: "company_type_Research & Development",
      desc: "Research & Development",
    },
    {
      sector: "company_type_Subsidiary or Business Segment",
      desc: "Subsidiary or Business Segment",
    },
    {
      sector: "company_type_Unknown / Non-Applicable",
      desc: "Unknown / Non-Applicable",
    },
    {
      sector: "company_sector_Unknown / Non-Applicable",
      desc: "sector_Unknown / Non-Applicable",
    },
    {
      sector: "company_sector_accounting & legal",
      desc: "sector_accounting & legal",
    },
    {
      sector: "company_sector_aerospace & defense",
      desc: "sector_aerospace & defense",
    },
    {
      sector: "company_sector_agriculture & forestry",
      desc: "sector_agriculture & forestry",
    },
    {
      sector: "company_sector_biotech & pharmaceuticals",
      desc: "sector_biotech & pharmaceuticals",
    },
    {
      sector: "company_sector_business services",
      desc: "sector_business services",
    },
    { sector: "company_sector_education", desc: "sector_education" },
    { sector: "company_sector_finance", desc: "sector_finance" },
    {
      sector: "company_sector_government",
      desc: "sector_government",
    },
    {
      sector: "company_sector_health care",
      desc: "sector_health care",
    },
    {
      sector: "company_sector_information technology",
      desc: "sector_information technology",
    },
    { sector: "company_sector_insurance", desc: "sector_insurance" },
    {
      sector: "company_sector_manufacturing",
      desc: "sector_manufacturing",
    },
    { sector: "company_sector_media", desc: "sector_media" },
    {
      sector: "company_sector_non-profit",
      desc: "sector_non-profit",
    },
    {
      sector: "company_sector_oil}, gas}, energy & utilities",
      desc: "sector_oil}, gas}, energy & utilities",
    },
    {
      sector: "company_sector_real estate",
      desc: "sector_real estate",
    },
    { sector: "company_sector_retail", desc: "sector_retail" },
    {
      sector: "company_sector_telecommunications",
      desc: "sector_telecommunications",
    },
    {
      sector: "company_sector_transportation & logistics",
      desc: "sector_transportation & logistics",
    },
    {
      sector: "company_sector_travel & tourism",
      desc: "sector_travel & tourism",
    },
  ];

  const [value, setValue] = React.useState("company_industry");
  const handleChange = (event) => {
    setValue(event.target.value);
  };

  const dispatch = useDispatch();
  const sector_redux = useSelector((state) => state.valueItemInForm.sector);

  return (
    <FormControl>
      <RadioGroup
        aria-labelledby="demo-controlled-radio-buttons-group"
        name="controlled-radio-buttons-group"
        value={sector_redux}
        onChange={(e) => {
          dispatch(chooseSector(e.target.value));
        }}
        row
      >
        {sectors.map((sect, i) => (
          <FormControlLabel
            value={sect.sector}
            control={<Radio />}
            key={i}
            label={sect.desc}
          />
        ))}
      </RadioGroup>
    </FormControl>
  );
}

export default SectorDescription;
