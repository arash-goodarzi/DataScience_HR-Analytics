import React from "react";
import { Radio, RadioGroup, FormControlLabel } from "@mui/material";
import Box from "@mui/material/Box";
import { useSelector, useDispatch } from "react-redux";
import { chooseIndustry } from "../../rootSlice";

function IndustryDescription(props) {
  const industries = [
    {
      industry: "company_industry_Accounting",
      desc: "Accounting",
    },
    {
      industry: "company_industry_Accounting & Legal",
      desc: "Accounting & Legal",
    },
    {
      industry: "company_industry_Advertising & Marketing",
      desc: "Advertising & Marketing",
    },
    {
      industry: "company_industry_Aerospace & Defense",
      desc: "Aerospace & Defense",
    },
    {
      industry: "company_industry_Airlines",
      desc: "Airlines",
    },
    {
      industry: "company_industry_Architectural & Engineering Services",
      desc: "Architectural & Engineering Services",
    },
    {
      industry: "company_industry_Banks & Credit Unions",
      desc: "Banks & Credit Unions",
    },
    {
      industry: "company_industry_Biotech & Pharmaceuticals",
      desc: "Biotech & Pharmaceuticals",
    },
    {
      industry: "company_industry_Brokerage Services",
      desc: "Brokerage Services",
    },
    {
      industry: "company_industry_Building & Personnel Services",
      desc: "Building & Personnel Services",
    },
    {
      industry: "company_industry_Business Service Centers & Copy Shops",
      desc: "Business Service Centers & Copy Shops",
    },
    {
      industry: "company_industry_Business Services",
      desc: "Business Services",
    },
    {
      industry: "company_industry_Cable}, Internet & Telephone Providers",
      desc: "Cable}, Internet & Telephone Providers",
    },
    {
      industry: "company_industry_Chemical Manufacturing",
      desc: "Chemical Manufacturing",
    },
    {
      industry: "company_industry_Colleges & Universities",
      desc: "Colleges & Universities",
    },
    {
      industry: "company_industry_Computer Hardware & Software",
      desc: "Computer Hardware & Software",
    },
    {
      industry: "company_industry_Consulting",
      desc: "Consulting",
    },
    {
      industry: "company_industry_Consumer Electronics & Appliances Stores",
      desc: "Consumer Electronics & Appliances Stores",
    },
    {
      industry: "company_industry_Consumer Products Manufacturing",
      desc: "Consumer Products Manufacturing",
    },
    {
      industry: "company_industry_Department}, Clothing}, & Shoe Stores",
      desc: "Department}, Clothing}, & Shoe Stores",
    },
    {
      industry: "company_industry_Education",
      desc: "Education",
    },
    {
      industry: "company_industry_Education Training Services",
      desc: "Education Training Services",
    },
    {
      industry: "company_industry_Electrical & Electronic Manufacturing",
      desc: "Electrical & Electronic Manufacturing",
    },
    { industry: "company_industry_Energy", desc: "Energy" },
    {
      industry: "company_industry_Enterprise Software & Network Solutions",
      desc: "Enterprise Software & Network Solutions",
    },
    {
      industry: "company_industry_Federal Agencies",
      desc: "Federal Agencies",
    },
    {
      industry: "company_industry_Food & Beverage Manufacturing",
      desc: "Food & Beverage Manufacturing",
    },
    {
      industry: "company_industry_Food & Beverage Stores",
      desc: "Food & Beverage Stores",
    },
    {
      industry: "company_industry_Food Production",
      desc: "Food Production",
    },
    {
      industry: "company_industry_General Merchandise & Superstores",
      desc: "General Merchandise & Superstores",
    },
    {
      industry: "company_industry_Government",
      desc: "Government",
    },
    {
      industry: "company_industry_Grocery Stores & Supermarkets",
      desc: "Grocery Stores & Supermarkets",
    },
    {
      industry: "company_industry_Health Care",
      desc: "Health Care",
    },
    {
      industry: "company_industry_Health Care Products Manufacturing",
      desc: "Health Care Products Manufacturing",
    },
    {
      industry: "company_industry_Health Care Services & Hospitals",
      desc: "Health Care Services & Hospitals",
    },
    {
      industry: "company_industry_Home Centers & Hardware Stores",
      desc: "Home Centers & Hardware Stores",
    },
    {
      industry: "company_industry_IT Services",
      desc: "IT Services",
    },
    {
      industry: "company_industry_Industrial Manufacturing",
      desc: "Industrial Manufacturing",
    },
    {
      industry: "company_industry_Information Technology",
      desc: "Information Technology",
    },
    {
      industry: "company_industry_Insurance Agencies & Brokerages",
      desc: "Insurance Agencies & Brokerages",
    },
    {
      industry: "company_industry_Internet",
      desc: "Internet",
    },
    {
      industry: "company_industry_Investment Banking & Asset Management",
      desc: "Investment Banking & Asset Management",
    },
    {
      industry: "company_industry_Lending",
      desc: "Lending",
    },
    {
      industry: "company_industry_Motion Picture Production & Distribution",
      desc: "Motion Picture Production & Distribution",
    },
    {
      industry: "company_industry_News Outlet",
      desc: "News Outlet",
    },
    {
      industry: "company_industry_Real Estate",
      desc: "Real Estate",
    },
    {
      industry: "company_industry_Religious Organizations",
      desc: "Religious Organizations",
    },
    {
      industry: "company_industry_Shipping",
      desc: "Shipping",
    },
    {
      industry: "company_industry_Staffing & Outsourcing",
      desc: "Staffing & Outsourcing",
    },
    {
      industry: "company_industry_Telecommunications Services",
      desc: "Telecommunications Services",
    },
    {
      industry: "company_industry_Transportation Equipment Manufacturing",
      desc: "Transportation Equipment Manufacturing",
    },
    {
      industry: "company_industry_Utilities",
      desc: "Utilities",
    },
  ];

  const [value, setValue] = React.useState("company_industry");
  const handleChange = (event) => {
    setValue(event.target.value);
  };
  const [selectedValue, setSelectedValue] = React.useState("a");

  const dispatch = useDispatch();
  const industry_redux = useSelector((state) => state.valueItemInForm.industry);

  return (
    <RadioGroup
      aria-labelledby="demo-controlled-radio-buttons-group"
      name="controlled-radio-buttons-group"
      value={industry_redux}
      onChange={(e) => dispatch(chooseIndustry(e.target.value))}
      row
    >
      <Box
        sx={{
          display: "flex",
          flexWrap: "wrap",

          justifyContent: "space-between",
          p: 1,
          m: 1,
          bgcolor: "background.paper",
          borderRadius: 1,
        }}
      >
        {industries.map((inds, i) => (
          <FormControlLabel
            value={inds.industry}
            control={<Radio />}
            key={i}
            label={inds.desc}
          />
        ))}
      </Box>
    </RadioGroup>
  );
}

export default IndustryDescription;
