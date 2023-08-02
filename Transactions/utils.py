def user_transaction_image_path(instance, filename):
    import os
    import jdatetime
    ext = filename.split(".")[-1]
    new_file_name = f"{jdatetime.date.today()}-{instance.transaction.user.id}.{ext}"
    return os.path.join("Transactions/offline-payment/", new_file_name)
