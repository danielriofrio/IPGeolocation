-- Table: public.ipgeolocationinfo

-- DROP TABLE public.ipgeolocationinfo;

CREATE TABLE public.ipgeolocationinfo
(
  ipnumberlow bigint NOT NULL,
  ipnumberhigh bigint NOT NULL,
  countrycode character varying(4),
  countryname character varying(50),
  region character varying(50),
  city character varying(50),
  latitude numeric,
  longitude numeric,
  zipcode character varying(10),
  timezone character varying(10),
  CONSTRAINT ipgeolocationinfo_pkey PRIMARY KEY (ipnumberlow, ipnumberhigh)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.ipgeolocationinfo
  OWNER TO ipgeolocation_usr;