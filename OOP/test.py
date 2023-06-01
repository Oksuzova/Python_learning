# -*- coding: cp1251 -*-1

import pytest
from lab_6 import *
from time import sleep


class TestDeviceParent:
    @pytest.fixture
    def device(self):
        return Device(100, 50)

    def test_device_attr(self, device):
        assert device.power == 100, "The power of the device does not match the expected"
        assert device.e_m_radiation == 50, "The electromagnetic radiation of the device does not match the expected"
        assert device.enable is False, "The state of device is not False after creating"

    def test_state_display(self, device):
        assert device.state() == "Disable", "The state of device displayed Enable"
        device.set_state(True)
        assert device.state() == "Enable", "The state of device displayed Disable"

    def test_device_power(self, device):
        assert device.power == 100
        device.power = 50
        assert device.power == 50

    def test_e_m_radiation(self, device):
        assert device.e_m_radiation == 50
        device.e_m_radiation = 100
        assert device.e_m_radiation == 100

    def test_device_state(self, device):
        assert device.enable is False
        device.set_state(True)
        assert device.enable is True

    def test_device_str(self, device):
        device_str = str(device)
        expected_str = f"Device: {device.name}, Power: {device.power} W, Electro-magnetic radiation: " \
                       f"{device.e_m_radiation} µW/cm2, state: {device.state()}"
        assert device_str == expected_str

    def test_device_repr(self, device):
        device_repr = repr(device)
        expected_repr = device.name
        assert device_repr == expected_repr


class TestDevice(TestDeviceParent):
    @pytest.fixture(params=[
        (Microwave),
        (WashingMachine),
        (Fridge),
        (Laptop)
    ])
    def device(self, request):
        sleep(1)
        return request.param(100, 50)


class TestDeviceManager:
    @pytest.fixture
    def manager(self):
        item1 = Microwave(500, 2)
        item2 = Laptop(200, 4)
        item3 = Fridge(300, 6)
        item4 = WashingMachine(400, 5)

        manager = DeviceManager()
        manager.set_items(item1, item2, item3, item4)
        return manager

    def test_get_items(self, manager):
        items = manager.get_items()
        assert len(items) == 4
        assert items[0].power == 500
        assert items[1].power == 200
        assert items[2].power == 300
        assert items[3].power == 400

    def test_sort_by_ascending(self, manager):
        items = manager.get_items()
        actual_result = manager.sort_by_ascending("Power")
        expected_result = [items[1], items[2], items[3], items[0]]
        assert actual_result == expected_result

    def test_sort_by_descending(self, manager):
        items = manager.get_items()
        actual_result = manager.sort_by_descending("e_m_radiation")
        expected_result = [items[2], items[3], items[1], items[0]]
        assert actual_result == expected_result

    def test_current_power(self, manager):
        items = manager.get_items()
        assert manager.current_power == 0
        for item in items:
            item.set_state(True)
        assert manager.current_power == 1400

    def test_check_radiation(self, manager):
        items = manager.get_items()
        actual_result = manager.check_radiation(4, 5)
        expected_result = [items[1], items[3]]
        assert actual_result == expected_result


