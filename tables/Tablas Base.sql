CREATE TABLE koob.users
(
    user_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    first_name character varying(255) COLLATE pg_catalog."default",
    last_name character varying(255) COLLATE pg_catalog."default",
    email character varying(255) COLLATE pg_catalog."default",
    phone character varying(12) COLLATE pg_catalog."default",
    passwd character varying(50) COLLATE pg_catalog."default",
    address character varying(255) COLLATE pg_catalog."default",
    puntos_koob integer,
    CONSTRAINT users_pkey PRIMARY KEY (user_id),
    CONSTRAINT unique_email UNIQUE (email)
);

CREATE TABLE koob.authors
(
    auth_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    first_name character varying(255) COLLATE pg_catalog."default",
    last_name character varying(255) COLLATE pg_catalog."default",
    year_of_birth date,
    country character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT authors_pkey PRIMARY KEY (auth_id)
);

CREATE TABLE koob.editorials
(
    ed_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    ed_name character varying(255) COLLATE pg_catalog."default",
    country character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT editorials_pkey PRIMARY KEY (ed_id)
);

CREATE TABLE koob.books
(
    book_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    ed_id integer NOT NULL,
    auth_id integer NOT NULL,
    pub_date date,
    genre character varying(20) COLLATE pg_catalog."default",
    gallery character varying(100) COLLATE pg_catalog."default",
    CONSTRAINT books_pkey PRIMARY KEY (book_name, ed_id, auth_id),
    CONSTRAINT books_auth_id_fkey FOREIGN KEY (auth_id)
        REFERENCES koob.authors (auth_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT books_ed_id_fkey FOREIGN KEY (ed_id)
        REFERENCES koob.editorials (ed_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE koob.publishes
(
    isbn character varying(13) COLLATE pg_catalog."default",
    book_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    ed_id integer NOT NULL,
    auth_id integer NOT NULL,
    CONSTRAINT publishes_pkey PRIMARY KEY (book_name, ed_id, auth_id),
    CONSTRAINT unique_isbn UNIQUE (isbn),
    CONSTRAINT fk_publishes FOREIGN KEY (ed_id, book_name, auth_id)
        REFERENCES koob.books (ed_id, book_name, auth_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);

CREATE TABLE koob.stock
(
    stock_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    auth_id integer NOT NULL,
    ed_id integer NOT NULL,
    book_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    b_condition smallint,
    price double precision,
    CONSTRAINT pk_stock PRIMARY KEY (stock_id, book_name, auth_id, ed_id),
    CONSTRAINT fk_stock FOREIGN KEY (ed_id, auth_id, book_name)
        REFERENCES koob.books (ed_id, auth_id, book_name) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT conditionrange CHECK (b_condition >= 1 AND b_condition <= 10),
    CONSTRAINT price CHECK (price >= 1::double precision)
);

CREATE TABLE koob.transaction
(
    transaction_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    stock_id integer NOT NULL,
    auth_id integer NOT NULL,
    ed_id integer NOT NULL,
    user_id integer NOT NULL,
    book_name character varying(255) COLLATE pg_catalog."default" NOT NULL,
    t_type character varying(9) COLLATE pg_catalog."default" NOT NULL,
    t_date date,
    CONSTRAINT pk_transaction PRIMARY KEY (transaction_id, stock_id, book_name, auth_id, ed_id, user_id),
    CONSTRAINT fk_stock FOREIGN KEY (book_name, ed_id, stock_id, auth_id)
        REFERENCES koob.stock (book_name, ed_id, stock_id, auth_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT fk_user FOREIGN KEY (user_id)
        REFERENCES koob.users (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT t_type_check CHECK (t_type::text = 'buying'::text OR t_type::text = 'selling'::text OR t_type::text = 'returning'::text)
);

