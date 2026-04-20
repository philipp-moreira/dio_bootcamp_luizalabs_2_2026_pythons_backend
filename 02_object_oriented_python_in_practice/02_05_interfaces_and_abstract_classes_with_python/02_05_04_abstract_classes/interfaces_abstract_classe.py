from abc import ABC, abstractmethod  # , abstractproperty #Obsolete since  python 3.3
import time


class RemoteControl(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    # @abstractproperty  # Obsolete since  python 3.3
    @property
    @abstractmethod
    def brand(self):
        pass

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {{{", ".join([f"'{k}': '{v}'" for k, v in self.__dict__.items()])}}}'


class TvControl(RemoteControl):
    def __init__(self, brand_tv):
        self._brand = brand_tv

    def on(self):
        print(f'{time.ctime()}\t-\tTV turning on...')
        time.sleep(2)
        print(f'{time.ctime()}\t-\tTV on!')

    def off(self):
        time.sleep(1)
        print(f'{time.ctime()}\t-\tTV turning of...')
        time.sleep(1)
        print(f'{time.ctime()}\t-\tTV of!')

    @property
    def brand(self):
        return self._brand


class AirConditionerControl(RemoteControl):
    def __init__(self, brand):
        self._brand = brand

    def on(self):
        print(f'{time.ctime()}\t-\tAir conditioner turning on...')
        time.sleep(2)
        print(f'{time.ctime()}\t-\tAir conditioner on!')

    def off(self):
        time.sleep(1)
        print(f'{time.ctime()}\t-\tAir conditioner turning off...')
        time.sleep(1)
        print(f'{time.ctime()}\t-\tAir conditioner off!')

    @property
    def brand(self):
        return self._brand


tv_control = TvControl('LG')
print(tv_control)
tv_control.on()

time.sleep(1)

ac_control = AirConditionerControl('Philco')
print(ac_control)
ac_control.on()
ac_control.off()
