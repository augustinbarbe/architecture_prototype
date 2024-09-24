from allocation.service_layer import unit_of_work
<<<<<<< HEAD
=======
from sqlalchemy.sql import text
>>>>>>> 8d65f899e6bb940b21165f045f1887534a12c693


def allocations(orderid: str, uow: unit_of_work.SqlAlchemyUnitOfWork):
    with uow:
        results = uow.session.execute(
<<<<<<< HEAD
            """
            SELECT sku, batchref FROM allocations_view WHERE orderid = :orderid
            """,
            dict(orderid=orderid),
        )
    return [dict(r) for r in results]
=======
            text(
                "SELECT sku, batchref FROM allocations_view WHERE orderid = :orderid"
            ),
            dict(orderid=orderid),
        )
    return [r._asdict() for r in results]
>>>>>>> 8d65f899e6bb940b21165f045f1887534a12c693
