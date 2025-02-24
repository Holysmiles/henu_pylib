class InsurancePolicy:
    def __init__(self, price_of_item):
        self.price_of_insured_item = price_of_item


class VehicleInsurance(InsurancePolicy):

    def __init__(self, vehicle_name, price_of_vehicle):
        super(VehicleInsurance, self).__init__(price_of_vehicle)
        self.vehicle_name = vehicle_name

    def get_rate(self):
        return float(self.price_of_insured_item) * 0.001


class HomeInsurance(InsurancePolicy):

    def __init__(self, mumber_number, price_of_home):
        super(HomeInsurance, self).__init__(price_of_home)
        self.home_local = mumber_number

    def get_rate(self):
        return float(self.price_of_insured_item) * 0.00005


if __name__ == "__main__":
    car_insurance = VehicleInsurance("MOTO", 20000)
    print(f"Vehicle Insurance Rate: {car_insurance.get_rate()}")

    # 创建一个HomeInsurance实例
    house_insurance = HomeInsurance(4, 300000)
    print(f"Home Insurance Rate: {house_insurance.get_rate()}")
