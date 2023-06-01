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
    def device_manager(self):
        return DeviceManager()


