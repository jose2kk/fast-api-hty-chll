CREATE TYPE currency_enum AS ENUM ('COP', 'USD');


CREATE TABLE companies (
    id uuid,
    name character varying(255) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    deleted_at timestamp with time zone DEFAULT NULL,
    PRIMARY KEY(id)
);


CREATE TABLE vacancies (
    id uuid,
    name character varying(255) NOT NULL,
    currency currency_enum NOT NULL,
    company_id uuid NOT NULL,
    salary float NOT NULL,
    vacancy_link character varying(255) NOT NULL,
    required_skills JSONB DEFAULT '[]'::jsonb NOT NULL,
    required_skills_dict JSONB DEFAULT '{}'::jsonb NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    deleted_at timestamp with time zone DEFAULT NULL,
    PRIMARY KEY(id),
    CONSTRAINT fk_company
        FOREIGN KEY(company_id)
	        REFERENCES companies(id)
);


CREATE TABLE users (
    id uuid,
    first_name character varying(40) NOT NULL,
    last_name character varying(40) NOT NULL,
    email character varying(50) UNIQUE NOT NULL,
    years_of_experience integer NOT NULL,
    skills JSONB DEFAULT '[]'::jsonb NOT NULL,
    skills_dict JSONB DEFAULT '{}'::jsonb NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    deleted_at timestamp with time zone DEFAULT NULL,
    PRIMARY KEY(id)
);
