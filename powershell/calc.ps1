function take_operand {
    $number1 = ''
    do {
        $parsed = [int]::TryParse((Read-Host 'Enter Number: '), [ref]$number1)
        if (-not $parsed) {
            Write-Host 'ERROR: Invalid input. Please enter a number.'
        }
    } while (-not $parsed)
    $number1
}

$continue_loop = $true

while ($continue_loop) {
    $operand1 = take_operand
    $operand2 = take_operand
    $operation = Read-Host 'Choose operation [+,-,*,/]'
    switch ($operation) {
        '-' {
            Write-Host 'Result: $($operand1 - $operand2)'
        }
        '+' {
            Write-Host 'Result: $($operand1 + $operand2)'
        }
        '*' {
            Write-Host 'Result: $($operand1 * $operand2)'
        }
        '/' {
            if ($operand2 -ne 0) {
                Write-Host 'Result: $($operand1 / $operand2)'
            }
            else {
                Write-Host 'ERROR: Division by zero is not allowed.'
            }
        }
        default {
            Write-Host 'Error: Invalid operation.'
        }
    }
    $continue_choice = Read-Host 'Continue? [Y/N]'
    if ($continue_choice -notmatch '^(Yes|Y)$') {
        $continue_loop = $false
    }
}