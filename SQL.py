class SQL_QUERY:
    IMAGE = "Select tbl_serie_plan.plan from tbl_serie_plan where tbl_serie_plan.name = "
    BODY = "Select body, body_p from fp where serie = "
    SEAT = "Select seat, seat_p from fp where serie = "