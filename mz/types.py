import click


class FloatRangeParamType(click.ParamType):
    name = 'float range'

    def __init__(self, min=None, max=None, clamp=False):
        self.min_ = min
        self.max_ = max
        self.clamp = clamp

    def convert(self, value, param, ctx):
        try:
            value = float(value)
        except ValueError:
            self.fail('%s is not a valid float' % value, param, ctx)
        else:
            if self.min_ and value < self.min_ and self.clamp:
                return self.min_
            elif self.min_ and value < self.min_ and not self.clamp:
                self.fail(
                    '%s is smaller than the minimum valid value %s.'
                    % (value, self.min_), param, ctx)
            elif self.max_ and value > self.max_ and self.clamp:
                return self.max_
            elif self.max_ and value > self.max_ and not self.clamp:
                self.fail(
                    '%s is bigger than the maximum valid value %s.'
                    % (value, self.max_), param, ctx)
            else:
                return value


FloatRange = FloatRangeParamType()
