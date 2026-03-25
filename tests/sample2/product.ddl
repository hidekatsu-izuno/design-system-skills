
```sql
CREATE TABLE product_category (
    category_id        BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    category_code      VARCHAR(30)  NOT NULL,
    category_name      VARCHAR(100) NOT NULL,
    parent_category_id BIGINT,
    sort_order         INTEGER      NOT NULL DEFAULT 0,
    is_active          BOOLEAN      NOT NULL DEFAULT TRUE,
    created_at         TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at         TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_product_category_code UNIQUE (category_code),
    CONSTRAINT fk_product_category_parent
        FOREIGN KEY (parent_category_id)
        REFERENCES product_category(category_id)
);

CREATE TABLE product (
    product_id            BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    product_code          VARCHAR(50)  NOT NULL,
    jan_code              VARCHAR(20),
    product_name          VARCHAR(200) NOT NULL,
    product_name_kana     VARCHAR(200),
    product_short_name    VARCHAR(100),
    category_id           BIGINT,
    product_type          VARCHAR(20)  NOT NULL DEFAULT 'NORMAL',
    unit_of_measure       VARCHAR(20)  NOT NULL DEFAULT 'EA',
    standard_unit_price   DECIMAL(12,2) NOT NULL DEFAULT 0,
    cost_price            DECIMAL(12,2) NOT NULL DEFAULT 0,
    tax_type              VARCHAR(20)  NOT NULL DEFAULT 'TAXABLE',
    tax_rate              DECIMAL(5,2) NOT NULL DEFAULT 10.00,
    stock_control_flag    BOOLEAN      NOT NULL DEFAULT TRUE,
    serial_control_flag   BOOLEAN      NOT NULL DEFAULT FALSE,
    lot_control_flag      BOOLEAN      NOT NULL DEFAULT FALSE,
    shelf_life_days       INTEGER,
    launch_date           DATE,
    end_of_sale_date      DATE,
    status                VARCHAR(20)  NOT NULL DEFAULT 'ACTIVE',
    remarks               VARCHAR(500),
    created_at            TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by            VARCHAR(50),
    updated_at            TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by            VARCHAR(50),
    version_no            BIGINT       NOT NULL DEFAULT 1,
    CONSTRAINT uq_product_code UNIQUE (product_code),
    CONSTRAINT uq_product_jan_code UNIQUE (jan_code),
    CONSTRAINT fk_product_category
        FOREIGN KEY (category_id)
        REFERENCES product_category(category_id),
    CONSTRAINT chk_product_type
        CHECK (product_type IN ('NORMAL', 'SERVICE', 'SET', 'OPTION')),
    CONSTRAINT chk_tax_type
        CHECK (tax_type IN ('TAXABLE', 'REDUCED', 'EXEMPT', 'NON_TAXABLE')),
    CONSTRAINT chk_status
        CHECK (status IN ('ACTIVE', 'SUSPENDED', 'ENDED')),
    CONSTRAINT chk_standard_unit_price
        CHECK (standard_unit_price >= 0),
    CONSTRAINT chk_cost_price
        CHECK (cost_price >= 0),
    CONSTRAINT chk_tax_rate
        CHECK (tax_rate >= 0),
    CONSTRAINT chk_shelf_life_days
        CHECK (shelf_life_days IS NULL OR shelf_life_days >= 0),
    CONSTRAINT chk_sale_period
        CHECK (
            end_of_sale_date IS NULL
            OR launch_date IS NULL
            OR launch_date <= end_of_sale_date
        )
);

CREATE INDEX idx_product_name
    ON product(product_name);

CREATE INDEX idx_product_category_id
    ON product(category_id);

CREATE INDEX idx_product_status
    ON product(status);
```