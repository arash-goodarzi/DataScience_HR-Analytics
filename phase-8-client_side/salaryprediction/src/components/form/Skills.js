import React from "react";
import {
  Radio,
  RadioGroup,
  Checkbox,
  FormControlLabel,
  FormGroup,
} from "@mui/material";
import Box from "@mui/material/Box";
import { useSelector, useDispatch } from "react-redux";
import { chooseToggleSkill } from "../../rootSlice";
import { chooseIndustry } from "../../rootSlice";

function SkillsDeails() {
  const skills_list = [
    { skill: "apache_airflow", desc: "apache_airflow" },
    { skill: "apache_kafka", desc: "apache_kafka" },
    { skill: "apache_camel", desc: "apache_camel" },
    { skill: "apache_oozie", desc: "apache_oozie" },
    { skill: "apache_nifi", desc: "apache_nifi" },
    { skill: "apache_spark", desc: "apache_spark" },
    { skill: "apache_drill", desc: "apache_drill" },
    { skill: "apache_hive", desc: "apache_hive" },
    { skill: "apache_streamsets", desc: "apache_streamsets" },
    { skill: "apache_flume", desc: "apache_flume" },
    { skill: "apache_lucerne", desc: "apache_lucerne" },
    { skill: "apache_hbase", desc: "apache_hbase" },
    { skill: "apache_hadoop", desc: "apache_hadoop" },
    { skill: "apache_ambari", desc: "apache_ambari" },
    { skill: "apache_solr", desc: "apache_solr" },
    { skill: "apache_flink", desc: "apache_flink" },
    { skill: "apache_zookeeper", desc: "apache_zookeeper" },
    { skill: "apache_mahout", desc: "apache_mahout" },
    { skill: "apache_sqoop", desc: "apache_sqoop" },
    { skill: "bigquery", desc: "bigquery" },
    { skill: "amazon_redshift", desc: "amazon_redshift" },
    { skill: "kinetica", desc: "kinetica" },
    { skill: "sql_server", desc: "sql_server" },
    { skill: "oracle", desc: "oracle" },
    { skill: "vertica", desc: "vertica" },
    { skill: "mindsdb", desc: "mindsdb" },
    { skill: "sql", desc: "sql" },
    { skill: "mongodb", desc: "mongodb" },
    { skill: "r", desc: "r" },
    { skill: "python", desc: "python" },
    { skill: "scala", desc: "scala" },
    { skill: "java", desc: "java" },
    { skill: "ms_office", desc: "ms_office" },
    { skill: "logstash", desc: "logstash" },
    { skill: "looker", desc: "looker" },
    { skill: "airflow", desc: "airflow" },
    { skill: "splunk", desc: "splunk" },
    { skill: "trifacta", desc: "trifacta" },
    { skill: "concurrency", desc: "concurrency" },
    { skill: "datarobot", desc: "datarobot" },
    { skill: "appdynamics", desc: "appdynamics" },
    { skill: "kanban", desc: "kanban" },
    { skill: "cyclotron", desc: "cyclotron" },
    { skill: "redash", desc: "redash" },
    { skill: "shell_scripting", desc: "shell_scripting" },
    { skill: "cython", desc: "cython" },
    { skill: "storm", desc: "storm" },
    { skill: "prometheus", desc: "prometheus" },
    { skill: "aws", desc: "aws" },
    { skill: "julia", desc: "julia" },
    { skill: "tableau", desc: "tableau" },
    { skill: "openrefine", desc: "openrefine" },
    { skill: "package_vs_module", desc: "package_vs_module" },
    { skill: "elasticsearch", desc: "elasticsearch" },
    { skill: "graphite", desc: "graphite" },
    { skill: "cassandra", desc: "cassandra" },
    { skill: "powerbi", desc: "powerbi" },
    { skill: "nlp", desc: "nlp" },
    { skill: "fivetran", desc: "fivetran" },
    { skill: "sap", desc: "sap" },
    { skill: "tensorflow", desc: "tensorflow" },
    { skill: "influxdb", desc: "influxdb" },
    { skill: "beats", desc: "beats" },
    { skill: "bigml", desc: "bigml" },
    { skill: "zabbix", desc: "zabbix" },
    { skill: "great_expectations", desc: "great_expectations" },
    { skill: "datacleaner", desc: "datacleaner" },
    { skill: "hevo", desc: "hevo" },
    { skill: "kibana", desc: "kibana" },
    { skill: "turbonomic", desc: "turbonomic" },
    { skill: "atlas.ti", desc: "atlas.ti" },
    { skill: "stitch", desc: "stitch" },
    { skill: "hpcc", desc: "hpcc" },
    { skill: "qlikview", desc: "qlikview" },
    { skill: "freeboard", desc: "freeboard" },
    { skill: "pandas", desc: "pandas" },
    { skill: "dashboardfox", desc: "dashboardfox" },
    { skill: "pentaho", desc: "pentaho" },
    { skill: "ado", desc: "ado" },
    { skill: "postgresql", desc: "postgresql" },
    { skill: "adaboosting", desc: "adaboosting" },
    { skill: "big_query", desc: "big_query" },
    { skill: "klipfolio", desc: "klipfolio" },
    { skill: "stats_iq", desc: "stats_iq" },
    { skill: "metaclasses", desc: "metaclasses" },
    { skill: "presto", desc: "presto" },
    { skill: "jenkins", desc: "jenkins" },
    { skill: "akka", desc: "akka" },
    { skill: "google_analytics", desc: "google_analytics" },
    { skill: "dynatrace", desc: "dynatrace" },
    { skill: "grafana", desc: "grafana" },
    { skill: "datadog", desc: "datadog" },
    { skill: "knime", desc: "knime" },
    { skill: "rapidminer", desc: "rapidminer" },
    { skill: "netdata", desc: "netdata" },
    { skill: "instana", desc: "instana" },
    { skill: "couchdb", desc: "couchdb" },
    { skill: "snowflake", desc: "snowflake" },
    { skill: "async.io", desc: "async.io" },
    { skill: "microstrategy", desc: "microstrategy" },
    { skill: "scrum", desc: "scrum" },
    { skill: "agile", desc: "agile" },
    { skill: "sas", desc: "sas" },
    { skill: "excel", desc: "excel" },
    { skill: "matlab", desc: "matlab" },
    { skill: "spss", desc: "spss" },
    { skill: "minitab", desc: "minitab" },
    { skill: "linear_regression", desc: "linear_regression" },
    { skill: "logistic_regression", desc: "logistic_regression" },
    { skill: "decision_tree", desc: "decision_tree" },
    { skill: "svm", desc: "svm" },
    { skill: "naive_bayes", desc: "naive_bayes" },
    { skill: "knn", desc: "knn" },
    { skill: "k-means", desc: "k-means" },
    { skill: "random_forest", desc: "random_forest" },
    { skill: "dimensionality_reduction", desc: "dimensionality_reduction" },
    { skill: "gradient_boosting", desc: "gradient_boosting" },
  ];

  const dispatch = useDispatch();
  const skills_redux = useSelector((state) => state.valueItemInForm.skills);

  console.log("--------------------------");
  console.log(skills_redux);
  console.log("--------------------------");

  return (
    <RadioGroup
      aria-labelledby="demo-controlled-radio-buttons-group"
      name="controlled-radio-buttons-group"
      value={skills_redux}
      // onChange={(e) => console.lognt(e.target.value)}
      // onChange={(e) => dispatch(chooseToggleSkill(e.target.value))}
      row
      value={["scala"]}
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
        {skills_list.map((skll, i) => (
          <FormControlLabel
            checked={skills_redux.includes(skll.skill)}
            control={
              <Checkbox
                value={skll.skill}
                onClick={(e) => dispatch(chooseToggleSkill(e.target.value))}
              />
            }
            key={i}
            label={skll.desc}
          />
        ))}
      </Box>
    </RadioGroup>
  );
}

export default SkillsDeails;
